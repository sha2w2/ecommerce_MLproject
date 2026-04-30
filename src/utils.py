import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, root_mean_squared_error


def evaluate_regression(y_true, y_pred, model_name="Model"):
    """Calculates and prints regression metrics."""
    mae = mean_absolute_error(y_true, y_pred)
    rmse = root_mean_squared_error(y_true, y_pred, squared=False)
    r2 = r2_score(y_true, y_pred)

    print(f"--- {model_name} Evaluation ---")
    print(f"MAE:  {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R2 Score: {r2:.2f}\n")
    return {"mae": mae, "rmse": rmse, "r2": r2}


def plot_pca_variance(pca, output_path):
    """Plots the explained variance of PCA components (Scree Plot)."""
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, len(pca.explained_variance_ratio_) + 1),
             pca.explained_variance_ratio_.cumsum(), marker='o', linestyle='--')
    plt.title("Cumulative Explained Variance by PCA Components")
    plt.xlabel("Number of Components")
    plt.ylabel("Cumulative Explained Variance")
    plt.grid()
    plt.savefig(output_path / "pca_variance_plot.png")
    plt.close()
