from ..models import CustomUser, Order, Wallet


def fetch_details_service(request):

    issue_type = request.data.get("issue_type")

    try:

        if issue_type == "ORDER_ISSUE":
            return handle_order_issue(request)

        elif issue_type == "PAYMENT_ISSUE":
            return handle_payment_issue(request)

        elif issue_type == "DELIVERY_ISSUE":
            return handle_delivery_issue(request)

        elif issue_type == "WALLET_ISSUE":
            return handle_wallet_issue(request)

        else:
            return {
                "data": None,
                "errors": {
                    "details": "Invalid issue type"
                },
                "status": 400
            }

    except Exception as e:

        return {
            "data": None,
            "errors": {
                "details": str(e)
            },
            "status": 500
        }
    
def handle_order_issue(request):

    email = request.data.get("email")
    order_id = request.data.get("order_id")

    user = CustomUser.objects.filter(
        email=email
    ).first()

    if not user:
        return {
            "data": None,
            "errors": {
                "details": "User not found"
            },
            "status": 404
        }

    order = Order.objects.filter(
        order_id=order_id,
        user=user
    ).prefetch_related(
        "order_items__product"
    ).first()

    if not order:
        return {
            "data": None,
            "errors": {
                "details": "Order not found"
            },
            "status": 404
        }

    items = []

    for item in order.order_items.all():

        items.append({
            "product_name": item.product.name,
            "quantity": item.quantity,
            "size": item.size,
            "price": str(item.price),
            "status": item.status,
        })

    return {
        "data": {
            "customer": {
                "name": user.username,
                "email": user.email,
            },

            "order": {
                "order_id": order.order_id,
                "status": order.status,
                "payment_status": order.payment_status,
                "payment_method": order.payment_method,
            },

            "items": items
        },

        "errors": None,
        "status": 200
    }

def handle_payment_issue(request):

    order_id = request.data.get("order_id")

    order = Order.objects.filter(
        order_id=order_id
    ).first()

    if not order:

        return {
            "data": None,
            "errors": {
                "details": "Order not found"
            },
            "status": 404
        }

    return {
        "data": {
            "payment_details": {
                "order_id": order.order_id,
                "payment_method": order.payment_method,
                "payment_status": order.payment_status,
                "razorpay_order_id": order.razorpay_order_id,
                "razorpay_payment_id": order.razorpay_payment_id,
                "total_amount": str(order.total_amount),
                "created_at": order.created_at,
            }
        },

        "errors": None,
        "status": 200
    }


def handle_delivery_issue(request):

    order_id = request.data.get("order_id")

    order = Order.objects.filter(
        order_id=order_id
    ).first()

    if not order:

        return {
            "data": None,
            "errors": {
                "details": "Order not found"
            },
            "status": 404
        }

    return {
        "data": {
            "delivery_details": {
                "order_id": order.order_id,
                "status": order.status,
                "full_name": order.full_name,
                "mobile": order.mobile,
                "district": order.district,
                "state": order.state,
                "pincode": order.pincode,
                "street_address": order.street_address,
                "payment_status": order.payment_status,
                "created_at": order.created_at,
            }
        },

        "errors": None,
        "status": 200
    }


def handle_wallet_issue(request):

    email = request.data.get("email")

    user = CustomUser.objects.filter(
        email=email
    ).first()

    if not user:

        return {
            "data": None,
            "errors": {
                "details": "User not found"
            },
            "status": 404
        }

    wallet = Wallet.objects.filter(
        user=user
    ).prefetch_related(
        "transactions"
    ).first()

    if not wallet:

        return {
            "data": None,
            "errors": {
                "details": "Wallet not found"
            },
            "status": 404
        }

    transactions = []

    for txn in wallet.transactions.all().order_by('-created_at')[:10]:

        transactions.append({
            "transaction_id": txn.transaction_id,
            "amount": str(txn.amount),
            "transaction_type": txn.transaction_type,
            "description": txn.description,
            "created_at": txn.created_at,
            "order_id": txn.order.order_id if txn.order else None,
        })

    return {
        "data": {
            "wallet": {
                "balance": str(wallet.balance),
                "transactions": transactions
            }
        },

        "errors": None,
        "status": 200
    }