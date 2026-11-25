import reader
import transformer


def test_read_csv():
    data = reader.read_csv("olist/olist_customers_dataset.csv")
    assert len(data) > 0


def test_to_snake_case():
    result = transformer.to_snake_case(["Customer ID", "Customer City"])
    assert result == ["customer_id", "customer_city"]


def test_calculate_order_totals():
    data = [
        {"order_id": "A1", "price": "100", "freight_value": "10"},
        {"order_id": "A1", "price": "200", "freight_value": "20"},
    ]

    result = transformer.calculate_order_totals(data)

    assert result["A1"] == 330

def test_read_csv_invalid_file():
    try:
        reader.read_csv("non_existing_file.csv")
    except reader.DataReadError:
        assert True
    else:
        assert False, "Expected DataReadError"


def test_to_snake_case_empty_list():
    result = transformer.to_snake_case([])
    assert result == []
