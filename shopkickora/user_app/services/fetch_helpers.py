def build_customer(user):

    return {

        "id": user.id,

        "username": user.username,

        "full_name": user.full_name,

        "email": user.email,

        "profile_image": user.profile_image_url,

        "email_verified": user.is_email_verified,

        "active": user.is_active,

        "blocked": user.is_blocked,

        "deleted": user.is_deleted,

        "referral_code": user.referral_code,

        "referred_by": (
            user.referred_by.email
            if user.referred_by
            else None
        )

    }

def build_shipping_address(order):

    return {

        "full_name": order.full_name,

        "mobile": order.mobile,

        "street_address": order.street_address,

        "district": order.district,

        "state": order.state,

        "country": order.country,

        "pincode": order.pincode,

    }

def build_saved_address(order):

    if not order.address:
        return None

    return {

        "full_name": order.address.full_name,

        "email": order.address.email,

        "mobile": order.address.mobile,

        "street_address": order.address.street_address,

        "district": order.address.district,

        "state": order.address.state,

        "country": order.address.country,

        "pincode": order.address.pincode,

        "is_default": order.address.is_default,

    }

def build_order(order):

    return {

        "order_id": order.order_id,

        "status": order.status,

        "payment_method": order.payment_method,

        "payment_status": order.payment_status,

        "razorpay_order_id": order.razorpay_order_id,

        "razorpay_payment_id": order.razorpay_payment_id,

        "razorpay_signature": order.razorpay_signature,

        "created_at": order.created_at.isoformat(),

        "coupon_code": order.coupon_code,

        "coupon_discount": str(order.coupon_discount),

        "shipping_charge": str(order.shipping_charge),

        "total_amount": str(order.total_amount),

        "final_total": str(order.final_total),

        "cancel_reason": order.cancel_reason,

    }

def build_product(product):

    return {

        "id": product.id,

        "name": product.name,

        "slug": product.slug,

        "description": product.description,

        "image": product.image_url,

        "brand": product.brand.name if product.brand else None,

        "category": product.category.name if product.category else None,

        "price": str(product.price),

        "discount_percentage": product.discount_percentage,

        "current_price": str(product.final_price),

        "offer_price": str(product.final_price_with_offer),

        "effective_discount": product.discount_percentage_effective,

        "stock": product.stock,

        "average_rating": product.average_rating,

        "reviews_count": product.reviews_count,

        "is_active": product.is_active,

    }

def build_order_item(item):

    return {

        "quantity": item.quantity,

        "size": item.size,

        "purchase_price": str(item.price),

        "status": item.status,

        "is_cancelled": item.is_cancelled,

        "cancel_reason": item.cancel_reason,

        "return_requested": item.is_return_requested,

        "return_approved": item.is_return_approved,

        "return_rejected": item.is_return_rejected,

        "return_reason": item.return_reason,

        "return_rejected_reason": item.return_rejected_reason,

        "return_requested_at": (
            item.return_requested_at.isoformat()
            if item.return_requested_at
            else None
        )

    }

def build_products(order):

    products = []

    for item in order.order_items.all():

        products.append({

            "product": build_product(item.product),

            "order_item": build_order_item(item)

        })

    return products

def build_wallet(wallet):

    if not wallet:
        return None

    transactions = []

    total_credit = 0

    total_debit = 0

    for txn in wallet.transactions.order_by("-created_at")[:10]:

        if txn.transaction_type == "CREDIT":
            total_credit += txn.amount
        else:
            total_debit += txn.amount

        transactions.append({

            "transaction_id": txn.transaction_id,

            "amount": str(txn.amount),

            "transaction_type": txn.transaction_type,

            "description": txn.description,

            "created_at": txn.created_at.isoformat(),

            "order_id": (
                txn.order.order_id
                if txn.order
                else None
            )

        })

    return {

        "balance": str(wallet.balance),

        "total_credit": str(total_credit),

        "total_debit": str(total_debit),

        "total_transactions": wallet.transactions.count(),

        "transactions": transactions,

    }

def build_summary(order):

    return {

        "total_products":
            order.order_items.count(),

        "cancelled_products":
            order.order_items.filter(
                is_cancelled=True
            ).count(),

        "returned_products":
            order.order_items.filter(
                is_return_requested=True
            ).count(),

        "ordered_products":
            order.order_items.filter(
                status="ORDERED"
            ).count(),

    }
def build_payment(order):

    return {

        "order_id": order.order_id,

        "payment_method": order.payment_method,

        "payment_status": order.payment_status,

        "razorpay_order_id": order.razorpay_order_id,

        "razorpay_payment_id": order.razorpay_payment_id,

        "razorpay_signature": order.razorpay_signature,

        "created_at": order.created_at.isoformat(),

    }

def build_billing(order):

    return {

        "subtotal": str(order.total_amount),

        "coupon_code": order.coupon_code,

        "coupon_discount": str(order.coupon_discount),

        "shipping_charge": str(order.shipping_charge),

        "grand_total": str(order.final_total),

    }

def build_delivery(order):

    return {

        "order_id": order.order_id,

        "delivery_status": order.status,

        "payment_status": order.payment_status,

        "payment_method": order.payment_method,

        "created_at": order.created_at.isoformat(),

        "shipping_charge": str(order.shipping_charge),

        "total_amount": str(order.total_amount),

        "final_total": str(order.final_total),

        "cancel_reason": order.cancel_reason,

    }

def build_wallet_summary(wallet):

    latest = (
        wallet.transactions.order_by("-created_at").first()
        if wallet.transactions.exists()
        else None
    )

    return {

        "wallet_exists": True,

        "has_transactions":
            wallet.transactions.exists(),

        "credit_transactions":
            wallet.transactions.filter(
                transaction_type="CREDIT"
            ).count(),

        "debit_transactions":
            wallet.transactions.filter(
                transaction_type="DEBIT"
            ).count(),

        "latest_transaction":
            latest.created_at.isoformat()
            if latest else None,

        "linked_orders":
            wallet.transactions.exclude(
                order=None
            ).count(),

    }