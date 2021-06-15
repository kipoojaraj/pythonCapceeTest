import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python"
)

mycursor = mydb.cursor()
delete_sql="TRUNCATE TABLE categories"
mycursor.execute(delete_sql)
delete_sql="TRUNCATE TABLE products"
mycursor.execute(delete_sql)


sql_t = "INSERT INTO categories (name) VALUES ('mobile'),('laptop'),('tablet')"
mycursor.execute(sql_t)
print(mycursor.rowcount, "was inserted in categories.")

sql = "INSERT INTO products(name, price, image,category_id) VALUES (%s, %s, %s, %s)"
val = [
  ('redmi note10 ', '12000','','1'),
  ('samsung ', '13000','','1'),
  ('oppoa31 ', '18000',' ','1'),
  ('HP', '44000','','2'),
  ('ASUS', '43000', '', '2'),
]
mycursor.executemany(sql, val)
print(mycursor.rowcount, "was inserted in products.")

select_sql="SELECT products.name,products.price,categories.name as category_name FROM products JOIN categories ON categories.id=products.category_id order by categories.name asc"
mycursor.execute(select_sql)
result = mycursor.fetchall()

cat_name = "";
for row in result:
  if(cat_name != row[2]):
    if(cat_name != ""):
      print("</ul>")

    cat_name = row[2]
    print("<ul>")
    print(cat_name)

  print("<li>")
  print(row[0] + " " + str(row[1]))
  print("</li>")


mydb.commit()

