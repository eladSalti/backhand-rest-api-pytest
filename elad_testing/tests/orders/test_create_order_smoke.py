import pytest
from elad_testing.src.dao.products_dao import ProductsDAO
from elad_testing.src.helpers.orders_helper import OrdersHelper
from elad_testing.src.dao.orders_dao import OrdersDAO

@pytest.mark.tcid48
def test_create_paid_order_guest_user():

    # get a ranndom product from db (by id)

    product_dao = ProductsDAO()
    order_helper = OrdersHelper()
    orders_dao = OrdersDAO()


    random_product = product_dao.get_random_product_from_db(1)
    product_id = random_product[0]['ID']

    # make the call
    # in this case we would like to use product that already exsits and we would get it from the db!
    info =  {"line_items": [
            {
              "product_id": product_id,
              "quantity": 1
            }
            ]}
    order_json = order_helper.create_order(additional_args=info)

    # verify response
    assert order_json, f"Create order response is empty"
    assert order_json['customer_id'] == 0, f"Create order as guest expected defult customer_id=0 but got '{order_json['customer_id']}'"
    assert len(order_json['line_items']) == 1, f"Expectet only 1 item in order but found '{len(order_json)}'"\
                                                f"Order id: {order_json['id']}"
    # verify db
    order_id = order_json['id']
    line_info = orders_dao.get_order_lines_by_order_id(order_id)
    assert line_info, f"Create order line item was not found in DB. Order ID {order_id}"

    line_items = [i for i in line_info if i['order_item_type'] == 'line_item']
    assert len(line_items) == 1, f"Expected 1 item but found {len(line_items)}. Order id: {order_id}"

    line_id = line_items[0]['order_item_id']
    line_details = orders_dao.get_order_items_details(line_id)
    db_product_id = line_details['_product_id']
    assert str(db_product_id) == str(product_id), f"Create order product_id in db does not match in API. API product id = {product_id}, DB product id: {db_product_id}"


