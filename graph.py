import matplotlib.pyplot as plt

def plot_accuracy_and_error(epochs, accuracy_values, error_values):
    plt.plot(epochs, accuracy_values, label='Accuracy', marker='o', color='b')
    plt.plot(epochs, error_values, label='Error', marker='x', color='r')
    plt.title('Model Accuracy and Error Over Epochs')
    plt.xlabel('Epochs')
    plt.ylabel('Metric Value')
    plt.grid(True)
    plt.legend()
    plt.show()

# Example data (replace these with your actual data)
epochs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
accuracy_values = [0.78, 0.82, 0.85, 0.87, 0.88, 0.89, 0.90, 0.91, 0.92, 0.93]
error_values = [0.22, 0.18, 0.15, 0.13, 0.12, 0.11, 0.10, 0.09, 0.08, 0.07]

plot_accuracy_and_error(epochs, accuracy_values, error_values)
import matplotlib.pyplot as plt

def plot_accuracy_and_error(epochs, accuracy_values, error_values):
    plt.plot(epochs, accuracy_values, label='Accuracy', marker='o', color='b')
    plt.plot(epochs, error_values, label='Error', marker='x', color='r')
    plt.title('Model Accuracy and Error ')
    plt.xlabel('Epochs')
    plt.ylabel('Metric Value')
    plt.grid(True)
    plt.legend()
    plt.show()

# Example data (replace these with your actual data)
epochs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
accuracy_values = [0.78, 0.82, 0.85, 0.87, 0.88, 0.89, 0.90, 0.91, 0.92, 0.93]
error_values = [0.22, 0.18, 0.15, 0.13, 0.12, 0.11, 0.10, 0.09, 0.08, 0.07]

plot_accuracy_and_error(epochs, accuracy_values, error_values)
