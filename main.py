from sklearn.datasets import fetch_rcv1

# Load the dataset
rcv1 = fetch_rcv1()

# rcv1.data → features (TF-IDF matrix)
# rcv1.target → labels (multi-label, sparse)
# rcv1.target_names → label names

print("Shape of data (TF-IDF vectors):", rcv1.data.shape)
print("Shape of labels (sparse multi-label):", rcv1.target.shape)
print("Sample target labels (first 5):", rcv1.target[:5])
