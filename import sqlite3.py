import sqlite3

# Menghubungkan ke database yang kamu pakai
conn = sqlite3.connect('portfolio.db')  # Ganti sesuai nama database kamu
cursor = conn.cursor()

# Nama tabel yang ingin diubah
table_name = 'projects'

# Nama dan tipe data kolom baru
new_column_name = 'screenshot'
new_column_type = 'TEXT'

# Query ALTER TABLE
alter_query = f"ALTER TABLE {table_name} ADD COLUMN {new_column_name} {new_column_type}"
cursor.execute(alter_query)

# Simpan perubahan
conn.commit()
conn.close()