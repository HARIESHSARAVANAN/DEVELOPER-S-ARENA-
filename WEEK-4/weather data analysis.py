
from pathlib import Path
import sys
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "weatherHistory.csv"
VIZ_DIR = BASE_DIR / "visualizations"

REQUIRED_COLUMNS = [
    "Formatted Date", "Summary", "Precip Type",
    "Temperature (C)", "Apparent Temperature (C)", "Humidity",
    "Wind Speed (km/h)", "Wind Bearing (degrees)", "Visibility (km)",
    "Loud Cover", "Pressure (millibars)", "Daily Summary"
]

def load_data(path: Path) -> pd.DataFrame:
    """Load the CSV with clear error handling."""
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    try:
        return pd.read_csv(path)
    except pd.errors.EmptyDataError as exc:
        raise ValueError("The dataset is empty.") from exc
    except Exception as exc:
        raise RuntimeError(f"Could not read dataset: {exc}") from exc

def validate_data(df: pd.DataFrame) -> None:
    """Validate required columns and basic data integrity."""
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    if df.empty:
        raise ValueError("Dataset contains no rows.")

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Convert dates, remove invalid dates/duplicates, and fill categories."""
    data = df.copy()
    data["Formatted Date"] = pd.to_datetime(
        data["Formatted Date"], utc=True, errors="coerce"
    )
    invalid_dates = data["Formatted Date"].isna().sum()
    if invalid_dates:
        print(f"Warning: removing {invalid_dates} invalid date rows.")
    data = data.dropna(subset=["Formatted Date"])
    duplicate_count = data.duplicated().sum()
    if duplicate_count:
        print(f"Removing {duplicate_count} exact duplicate rows.")
    data = data.drop_duplicates()
    data["Precip Type"] = data["Precip Type"].fillna("Unknown")
    data["Year"] = data["Formatted Date"].dt.year
    data["Month"] = data["Formatted Date"].dt.month
    data["Hour"] = data["Formatted Date"].dt.hour
    return data

def analyze(data: pd.DataFrame) -> None:
    """Print key descriptive statistics and relationships."""
    print("\n" + "=" * 60)
    print("WEATHER DATA ANALYSIS")
    print("=" * 60)
    print(f"Rows after cleaning : {len(data):,}")
    print(f"Date range          : {data['Formatted Date'].min()} to {data['Formatted Date'].max()}")

    print("\nDescriptive statistics:")
    cols = [
        "Temperature (C)", "Apparent Temperature (C)",
        "Humidity", "Wind Speed (km/h)", "Visibility (km)"
    ]
    print(data[cols].describe().round(2))

    corr = data["Temperature (C)"].corr(data["Humidity"])
    print(f"\nTemperature/Humidity correlation: {corr:.3f}")

    print("\nMost common weather conditions:")
    print(data["Summary"].value_counts().head(8))

def create_visualizations(data: pd.DataFrame) -> None:
    """Create four chart types and save them as PNG files."""
    VIZ_DIR.mkdir(exist_ok=True)

    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    monthly = data.groupby("Month")["Temperature (C)"].mean().reindex(range(1, 13))

    plt.figure(figsize=(11, 6))
    plt.plot(monthly.index, monthly.values, marker="o")
    plt.xticks(range(1, 13), months)
    plt.xlabel("Month")
    plt.ylabel("Average Temperature (°C)")
    plt.title("Average Temperature by Month")
    plt.grid(True, alpha=0.25)
    plt.tight_layout()
    plt.savefig(VIZ_DIR / "01_average_temperature_by_month.png", dpi=180)
    plt.close()

    counts = data["Summary"].value_counts().head(8).sort_values()
    plt.figure(figsize=(11, 6))
    counts.plot(kind="barh")
    plt.xlabel("Number of Records")
    plt.ylabel("Weather Summary")
    plt.title("Top 8 Weather Conditions")
    plt.tight_layout()
    plt.savefig(VIZ_DIR / "02_top_weather_conditions.png", dpi=180)
    plt.close()

    sample = data.sample(min(5000, len(data)), random_state=42)
    plt.figure(figsize=(10, 6))
    plt.scatter(sample["Temperature (C)"], sample["Humidity"], alpha=0.25, s=10)
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Humidity")
    plt.title("Temperature vs Humidity")
    plt.grid(True, alpha=0.2)
    plt.tight_layout()
    plt.savefig(VIZ_DIR / "03_temperature_vs_humidity.png", dpi=180)
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.hist(data["Temperature (C)"], bins=30)
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Frequency")
    plt.title("Temperature Distribution")
    plt.grid(True, alpha=0.2)
    plt.tight_layout()
    plt.savefig(VIZ_DIR / "04_temperature_distribution.png", dpi=180)
    plt.close()

def main() -> int:
    try:
        raw = load_data(DATA_PATH)
        validate_data(raw)
        cleaned = clean_data(raw)
        if cleaned.empty:
            raise ValueError("No valid rows remain after cleaning.")
        analyze(cleaned)
        create_visualizations(cleaned)
        print("\nAnalysis completed successfully.")
        print(f"Charts saved to: {VIZ_DIR}")
        return 0
    except (FileNotFoundError, ValueError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
