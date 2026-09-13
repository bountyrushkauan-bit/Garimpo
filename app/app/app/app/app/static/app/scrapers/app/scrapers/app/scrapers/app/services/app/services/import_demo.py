from sqlalchemy.orm import Session

from ..models import Product
from ..scrapers.demo import demo_products


def import_demo(db: Session) -> int:
    products = demo_products()

    for item in products:
        product = Product(
            name=item.name,
            category=item.category,
            store=item.store,
            url=item.url,
            price=item.price,
            old_price=item.old_price,
            is_deal=item.is_deal,
        )

        db.add(product)

    db.commit()

    return len(products)
