# -*- coding: utf-8 -*-
"""
Author:         Ouyang_Yibei <said047@163.com>
Filename:       auction
Date Created:   2015-12-15 10:41
Description:

"""
from utils.http import ProtobufResponse

from core.auction import AuctionManager

from protomsg.auction_pb2 import (
    StaffAuctionSearchResponse,
    StaffAuctionSellResponse,
    StaffAuctionCancelResponse,
    StaffAuctionBiddingResponse,
)


def search(request):
    server_id = request._game_session.server_id
    char_id = request._game_session.char_id

    auction = AuctionManager(server_id, char_id)
    items = auction.search()

    response = StaffAuctionSearchResponse()
    response.ret = 0
    for item in items:
        response_item = response.items.add()
        response_item.MergeFrom(item.make_proto_msg())

    return ProtobufResponse(response)


def sell(request):
    server_id = request._game_session.server_id
    char_id = request._game_session.char_id

    staff_id = request._proto.staff_id
    tp = request._proto.tp
    min_price = request._proto.min_price
    max_price = request._proto.max_price

    auction = AuctionManager(server_id, char_id)
    auction.sell(staff_id, tp, min_price, max_price)

    response = StaffAuctionSellResponse()
    response.ret = 0

    return ProtobufResponse(response)


def cancel(request):
    server_id = request._game_session.server_id
    char_id = request._game_session.char_id

    item_id = request._proto.item_id

    auction = AuctionManager(server_id, char_id)
    auction.cancel(item_id)

    response = StaffAuctionCancelResponse()
    response.ret = 0

    return ProtobufResponse(response)


def bidding(request):
    server_id = request._game_session.server_id
    char_id = request._game_session.char_id

    item_id = request._proto.item_id
    price = request._proto.price

    auction = AuctionManager(server_id, char_id)
    auction.bidding(item_id, price)

    response = StaffAuctionBiddingResponse()
    response.ret = 0

    return ProtobufResponse(response)
