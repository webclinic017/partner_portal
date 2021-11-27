from django.db import connections

cursor = connections['erp'].cursor()

query = "SELECT `v_products_analysis_balances`.`service_product_id`, `service_products`.`title`, `service_products`.`minimum_inventory` AS minimum_inventory, `service_products`.`maximum_inventory` AS maximum_inventory, `service_products`.`alert_inventory` AS alert_inventory, SUM(`v_products_analysis_balances`.`in_stock`) AS in_stock, CASE WHEN in_stock >= maximum_inventory THEN 'MAX' WHEN in_stock <= minimum_inventory THEN 'MIN' WHEN in_stock <= alert_inventory THEN 'ALERTA' WHEN in_stock > alert_inventory AND in_stock < maximum_inventory THEN 'NORMAL' ELSE 'OTHER' END AS status FROM `dbemp00359`.`v_products_analysis_balances` INNER JOIN `dbemp00359`.`service_products` ON `v_products_analysis_balances`.`service_product_id` = `service_products`.`id` GROUP BY `v_products_analysis_balances`.`service_product_id` HAVING status = 'ALERTA'"

cursor.execute(query)

rows = cursor.fetchall()
json_data = []
for row in rows:
    json_data.append({"winner" : row[0], "count" : row[1]})


# from django.http import JsonResponse
# from django.db import connections
# from django.http import HttpResponse
# import json

# def testRawQuery(request):
#     cursor = connections['default'].cursor()
#     cursor.execute("select winner,count(winner) as count from DB")
#     objs = cursor.fetchall() 
#     json_data = []
#     for obj in objs:
#         json_data.append({"winner" : obj[0], "count" : obj[1]})
#     return JsonResponse(json_data, safe=False)