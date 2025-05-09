import os
import random
import shutil

# Configuration
input_root  = "corpus"
train_root  = "corpus_train"
test_root   = "corpus_test"
train_ratio = 0.8  # 80% train, 20% test

for genre in os.listdir(input_root):
    src_dir = os.path.join(input_root, genre)
    if not os.path.isdir(src_dir):
        continue

    # Ensure output genre folders exist
    os.makedirs(os.path.join(train_root, genre), exist_ok=True)
    os.makedirs(os.path.join(test_root,  genre), exist_ok=True)

    # List and shuffle files
    files = [f for f in os.listdir(src_dir) if f.endswith(".txt")]
    random.shuffle(files)

    # Split index
    split_idx = int(len(files) * train_ratio)
    train_files = files[:split_idx]
    test_files  = files[split_idx:]

    # Copy files
    for fname in train_files:
        shutil.copy(
            os.path.join(src_dir, fname),
            os.path.join(train_root, genre, fname)
        )
    for fname in test_files:
        shutil.copy(
            os.path.join(src_dir, fname),
            os.path.join(test_root,  genre, fname)
        )

    print(f"{genre}: {len(train_files)} train / {len(test_files)} test")
