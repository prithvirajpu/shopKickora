from ..models import CustomUser, Order, Wallet
from .fetch_helpers import (
    build_customer,
    build_order,
    build_shipping_address,
    build_saved_address,
    build_products,
    build_summary,
    build_payment,
    build_billing,
    build_wallet,
    build_delivery,
    build_wallet_summary,
)

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

    order = (
        Order.objects.filter(
            order_id=order_id,
            user=user
        )
        .select_related(
            "address"
        )
        .prefetch_related(
            "order_items__product__brand",
            "order_items__product__category",
            "order_items__product__reviews",
        )
        .first()
    )

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

            "customer": build_customer(user),

            "order": build_order(order),

            "shipping_address":
                build_shipping_address(order),

            "saved_address":
                build_saved_address(order),

            "products":
                build_products(order),

            "summary":
                build_summary(order),

        },

        "errors": None,

        "status": 200

    }

def handle_payment_issue(request):

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

    order = (
        Order.objects.filter(
            order_id=order_id,
            user=user
        )
        .select_related(
            "address"
        )
        .prefetch_related(
            "order_items__product__brand",
            "order_items__product__category",
            "order_items__product__reviews",
        )
        .first()
    )

    if not order:
        return {
            "data": None,
            "errors": {
                "details": "Order not found"
            },
            "status": 404
        }

    wallet = (
        Wallet.objects.filter(
            user=user
        )
        .prefetch_related(
            "transactions__order"
        )
        .first()
    )

    return {

        "data": {

            "customer":
                build_customer(user),

            "payment":
                build_payment(order),

            "billing":
                build_billing(order),

            "order":
                build_order(order),

            "shipping_address":
                build_shipping_address(order),

            "saved_address":
                build_saved_address(order),

            "wallet":
                build_wallet(wallet),

            "products":
                build_products(order),

            "summary": {

                **build_summary(order),

                "payment_completed":
                    order.payment_status == "paid",

                "payment_pending":
                    order.payment_status == "pending",

                "payment_failed":
                    order.payment_status == "failed",

                "wallet_exists":
                    wallet is not None,

                "wallet_balance":
                    str(wallet.balance)
                    if wallet else "0.00"

            }

        },

        "errors": None,

        "status": 200

    }

def handle_delivery_issue(request):

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

    order = (
        Order.objects.filter(
            order_id=order_id,
            user=user
        )
        .select_related(
            "address"
        )
        .prefetch_related(
            "order_items__product__brand",
            "order_items__product__category",
            "order_items__product__reviews",
        )
        .first()
    )

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

            "customer": build_customer(user),

            "delivery": build_delivery(order),

            "shipping_address": build_shipping_address(order),

            "saved_address": build_saved_address(order),

            "products": build_products(order),

            "summary": {

                **build_summary(order),

                "delivery_completed":
                    order.status == "DELIVERED",

                "delivery_pending":
                    order.status == "PENDING",

                "delivery_shipped":
                    order.status == "SHIPPED",

                "out_for_delivery":
                    order.status == "OUT_FOR_DELIVERY",

                "delivery_cancelled":
                    order.status == "CANCELLED",

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

    wallet = (
        Wallet.objects.filter(
            user=user
        )
        .prefetch_related(
            "transactions__order"
        )
        .first()
    )

    if not wallet:
        return {
            "data": None,
            "errors": {
                "details": "Wallet not found"
            },
            "status": 404
        }

    return {

        "data": {

            "customer": build_customer(user),

            "wallet": build_wallet(wallet),

            "summary": build_wallet_summary(wallet),

        },

        "errors": None,

        "status": 200

    }