from .BaseRecord import BaseRecord


def extract_data_by_position(data, position, byte):
    """
    指定された位置とバイト数に基づいてデータの部分文字列を返す。

    :param data: 元となるデータ文字列
    :param position: 開始位置(1から始まる)
    :param byte: 取得するバイト数
    :return: 指定された位置とバイト数に基づく部分文字列
    """
    start_index = position - 1  # Pythonのインデックスは0から始まるため調整
    end_index = start_index + byte
    return data[start_index:end_index]


class SingleVoteCount(BaseRecord):
    """単数票数"""

    def __init__(self, data):
        self.horse_number = extract_data_by_position(data, 1, 2)
        self.vote_count = extract_data_by_position(data, 3, 11)
        self.popularity_rank = extract_data_by_position(data, 14, 2)


class PlaceVoteCount(BaseRecord):
    """複勝票数"""

    def __init__(self, data):
        self.horse_number = extract_data_by_position(data, 1, 2)
        self.vote_count = extract_data_by_position(data, 3, 11)
        self.popularity_rank = extract_data_by_position(data, 14, 2)


class BracketQuinellaVoteCount(BaseRecord):
    """枠連票数"""

    def __init__(self, data):
        self.pair_number = extract_data_by_position(data, 1, 2)
        self.vote_count = extract_data_by_position(data, 3, 11)
        self.popularity_rank = extract_data_by_position(data, 14, 2)


class QuinellaVoteCount(BaseRecord):
    """馬連票数"""

    def __init__(self, data):
        self.pair_number = extract_data_by_position(data, 1, 4)
        self.vote_count = extract_data_by_position(data, 5, 11)
        self.popularity_rank = extract_data_by_position(data, 16, 3)


class WideVoteCount(BaseRecord):
    """ワイド票数"""

    def __init__(self, data):
        self.pair_number = extract_data_by_position(data, 1, 4)
        self.vote_count = extract_data_by_position(data, 5, 11)
        self.popularity_rank = extract_data_by_position(data, 16, 3)


class ExactaVoteCount(BaseRecord):
    """馬単票数"""

    def __init__(self, data):
        self.pair_number = extract_data_by_position(data, 1, 4)
        self.vote_count = extract_data_by_position(data, 5, 11)
        self.popularity_rank = extract_data_by_position(data, 16, 3)


class TrioVoteCount(BaseRecord):
    """3連複票数"""

    def __init__(self, data):
        self.pair_number = extract_data_by_position(data, 1, 6)
        self.vote_count = extract_data_by_position(data, 7, 11)
        self.popularity_rank = extract_data_by_position(data, 18, 3)


class H1Record(BaseRecord):
    """確定票数(3連単以外)"""

    def __init__(self, data):
        self.record_type = extract_data_by_position(data, 1, 2)
        self.data_kind = extract_data_by_position(data, 3, 1)
        self.create_date_data = extract_data_by_position(data, 4, 8)
        self.holding_year = extract_data_by_position(data, 12, 4)
        self.holding_date = extract_data_by_position(data, 16, 4)
        self.racecourse_code = extract_data_by_position(data, 20, 2)
        self.holding_number = extract_data_by_position(data, 22, 2)
        self.day_of_holding = extract_data_by_position(data, 24, 2)
        self.race_number = extract_data_by_position(data, 26, 2)
        self.registered_horse_count = extract_data_by_position(data, 28, 2)
        self.starting_horse_count = extract_data_by_position(data, 30, 2)
        self.win_betting_flag = extract_data_by_position(data, 32, 1)
        self.place_betting_flag = extract_data_by_position(data, 33, 1)
        self.bracket_quinella_betting_flag = extract_data_by_position(data, 34, 1)
        self.quinella_betting_flag = extract_data_by_position(data, 35, 1)
        self.wide_betting_flag = extract_data_by_position(data, 36, 1)
        self.exacta_betting_flag = extract_data_by_position(data, 37, 1)
        self.trio_betting_flag = extract_data_by_position(data, 38, 1)
        self.place_payout_key = extract_data_by_position(data, 39, 1)
        # 返還馬番情報
        self.return_horse_number_info = [
            extract_data_by_position(data, 40 + i, 1) for i in range(28)
        ]
        # 返還枠番情報
        self.return_frame_number_info = [
            extract_data_by_position(data, 68 + i, 1) for i in range(8)
        ]
        # 返還同枠情報
        self.return_same_frame_number_info = [
            extract_data_by_position(data, 76 + i, 1) for i in range(8)
        ]
        # 単勝票数
        self.single_vote_count = [
            SingleVoteCount(extract_data_by_position(data, 84 + i * 15, 15))
            for i in range(28)
        ]
        # 複勝票数
        self.place_vote_count = [
            PlaceVoteCount(extract_data_by_position(data, 504 + i * 15, 15))
            for i in range(28)
        ]
        # 枠連票数
        self.bracket_quinella_vote_count = [
            BracketQuinellaVoteCount(extract_data_by_position(data, 924 + i * 15, 15))
            for i in range(36)
        ]
        # 馬連票数
        self.quinella_vote_count = [
            QuinellaVoteCount(extract_data_by_position(data, 1464 + i * 18, 18))
            for i in range(153)
        ]
        # ワイド票数
        self.wide_vote_count = [
            WideVoteCount(extract_data_by_position(data, 4218 + i * 18, 18))
            for i in range(153)
        ]
        # 馬単票数
        self.exacta_vote_count = [
            ExactaVoteCount(extract_data_by_position(data, 6972 + i * 18, 18))
            for i in range(306)
        ]
        # 3連複票数
        self.trio_vote_count = [
            TrioVoteCount(extract_data_by_position(data, 12480 + i * 20, 20))
            for i in range(816)
        ]
        self.total_single_vote_count = extract_data_by_position(data, 28800, 11)
        self.total_place_voite_count = extract_data_by_position(data, 28811, 11)
        self.total_bracket_quinella_vote_count = extract_data_by_position(
            data, 28822, 11
        )
        self.total_quinella_vote_count = extract_data_by_position(data, 28833, 11)
        self.total_wide_vote_count = extract_data_by_position(data, 28844, 11)
        self.total_exacta_vote_count = extract_data_by_position(data, 28855, 11)
        self.total_trio_vote_count = extract_data_by_position(data, 28866, 11)
        self.total_win_refund_vote_count = extract_data_by_position(data, 28877, 11)
        self.total_place_refund_vote_count = extract_data_by_position(data, 28888, 11)
        self.total_bracket_quinella_refund_vote_count = extract_data_by_position(
            data, 28899, 11
        )
        self.total_quinella_refund_vote_count = extract_data_by_position(
            data, 28910, 11
        )
        self.total_wide_refund_vote_count = extract_data_by_position(data, 28921, 11)
        self.total_exacta_refund_vote_count = extract_data_by_position(data, 28932, 11)
        self.total_trio_refund_vote_count = extract_data_by_position(data, 28943, 11)
