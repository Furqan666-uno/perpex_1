from celery import shared_task
from django.db.models import Sum, Count
from .models import Order, MenuItem, SalesReport

@shared_task
def generate_sales_report():
    total_sales= Order.objects.aggregate(total=Sum("amount"))["total"] or 0

    # top selling item
    top_item= (Order.objects.values("product_name").annotate(count=Count("id")).order_by("-count").first())
    top_item_name= top_item["product_name"] if top_item else "No Sales"

    SalesReport.objects.create(total_sales=total_sales, top_item=top_item_name)
    return f"Report generated: Sales={total_sales}, Top Item={top_item_name}"
