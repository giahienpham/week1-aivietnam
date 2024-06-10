def md_nre_single_sample(y, y_hat, n, p):
    y_root = y ** (1/n)
    y_hat_root = y_hat ** (1/n)
    difference = abs(y_root - y_hat_root)**p
    return difference

print(f"md_nre_single_sample(y=100, y_hat=99.5, n=2, p=1)")
print(f">> {md_nre_single_sample(100, 99.5, 2, 1)}")

print(f"md_nre_single_sample(y=50, y_hat=49.5, n=2, p=1)")
print(f">> {md_nre_single_sample(50, 49.5, 2, 1)}")

print(f"md_nre_single_sample(y=20, y_hat=19.5, n=2, p=1)")
print(f">> {md_nre_single_sample(20, 19.5, 2, 1)}")

print(f"md_nre_single_sample(y=0.6, y_hat=0.1, n=2, p=1)")
print(f">> {md_nre_single_sample(0.6, 0.1, 2, 1)}")

print(f"md_nre_single_sample(y=1, y_hat=6   , n=2, p=1)")
print(f">> {md_nre_single_sample(0.6, 0.1, 2, 1)}")
