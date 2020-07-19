import pandas as pd
import numpy as np

data = pd.DataFrame({
    "id":[x for x in np.random.randint(0,50,20)] ,
    "age":np.random.randint(15,50,20),
    "order_id":np.random.randint(5,50,20),
    })
#1. SELECT * FROM data;
print(data)
# 2. SELECT * FROM data LIMIT 10;
print(data.head(10))
# 3. SELECT id FROM data;  //id 是 data 表的特定一列
print(data['id'])
# 4. SELECT COUNT(id) FROM data;
print(data['id'].count())
# 5. SELECT * FROM data WHERE id<1000 AND age>30;
print(data[(data['id']<1000) & (data['age']>30)])
# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
data_drop = data.drop_duplicates('order_id',keep='first')
data_group = data_drop.groupby('id').count()
data_group['order_id']
# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
pd.merge(table1,table2,on='id',how='inner')
# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
pd.concat(table1,table2)
# 9. DELETE FROM table1 WHERE id=10;
data.drop(data[data['id']==0].index)
# 10. ALTER TABLE table1 DROP COLUMN column_name;
data.drop('age',axis=1)
