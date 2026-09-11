import csv
import secrets
import subprocess

with open("users_in.csv", newline="") as f_in, open("users_out.csv", "w", newline="") as f_out:
    reader = csv.DictReader(f_in)
    writer = csv.DictWriter(f_out, fieldnames=reader.fieldnames)
    writer.writeheader()

    created, failed = 0, 0
    for row in reader:
        username = row["username"].strip()
        if not username:
            continue

        row["password"] = secrets.token_hex(8)

        result = subprocess.run(
            ["/usr/sbin/useradd", username],
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            created += 1
            writer.writerow(row)
            print(f"✅ Created: {username}")
        else:
            failed += 1
            print(f"❌ Failed: {username} — {result.stderr.strip()}")

print(f"\nDone. Created: {created}, Failed: {failed}")