import orders_requests
import data


def test_new_order_status_received():
    response = orders_requests.new_order_create(data.BODY_ORDER)
    assert response.status_code == 201
    track = str(response.json()["track"])
    received_track = orders_requests.get_order_status(track)
    assert received_track.status_code == 200
