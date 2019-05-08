from model import *
import json
import time


class DataUtil:

    @staticmethod
    def get_user_info(user_id: int):
        try:
            return User.get(User.id == user_id)
        except User.DoseNotExist:
            return False

    @staticmethod
    def get_page_record(user_id: int, restaurant_id: int, page_id: int):
        try:
            return PageRecord.get((PageRecord.user_id == user_id)
                                  & (PageRecord.restaurant_id == restaurant_id)
                                  & (PageRecord.page_id == page_id))
        except PageRecord.DoesNotExist:
            return False

    @staticmethod
    def get_one_question(question_id: int):
        try:
            return Question.get(Question.id == question_id)
        except Question.DoesNotExist:
            return False

    @staticmethod
    def get_all_questions(restaurant_id: int):
        _questions = []
        _question_ids = []
        _page_id = 0
        try:
            _page = Page.get(Page.restaurant_id == restaurant_id)
            _question_ids = json.loads(_page.questions)
        except Page.DoesNotExist:
            pass
        except json.decoder.JSONDecodeError:
            pass
        if len(_question_ids):
            _id_str = ",".join(str(s) for s in _question_ids)
            _sql = "select id, question, type from question where id in(" + _id_str + ") order by instr('," + _id_str + ",', ','||id||',')"
            _questions = list(Question.raw(_sql))
            _page_id = _page.id

            _options = Option.select().where(Option.question_id in _question_ids).order_by(Option.question_id, Option)
            _option_array = {}
            for _opt in _options:
                _key = str(_opt.question_id)
                if _key not in _option_array.keys():
                    _option_array[_key] = []
                _option_array[_key].append({
                    'option': _opt.option,
                    'value': int(_opt.value),
                    'score': int(_opt.score),
                })

            for _q in _questions:
                if str(_q.id) not in _option_array.keys():
                    _q.option = []
                else:
                    _q.option = _option_array[str(_q.id)]

        return _questions, _page_id

    @staticmethod
    def get_restaurant_info(restaurant_id: int):
        try:
            return Restaurant.get(Restaurant.id == restaurant_id)
        except Restaurant.DoseNotExist:
            return False

    @staticmethod
    def get_answers(user_id: int, restaurant_id: int):
        _answers = []
        _page_id = 0
        try:
            _data = PageRecord.select(PageRecord.page_id)\
                .where((PageRecord.user_id == user_id) & (PageRecord.restaurant_id == restaurant_id))\
                .order_by(PageRecord.id.desc())\
                .limit(1)\
                .namedtuples()
        except PageRecord.DoseNotExist:
            pass

        for _row in _data:
            _page_id = _row.page_id

        if _page_id:
            _list = Answer.select(Question.id, Question.question, Answer.answer, Answer.score, Answer.value)\
                .join(Question, on=(Question.id == Answer.question_id))\
                .where((Answer.user_id == user_id) & (Answer.restaurant_id == restaurant_id) & (Answer.page_id == _page_id))\
                .namedtuples()

        for _row in _list:
            _answers.append({
                'id': _row.id,
                'question': _row.question,
                'answer': _row.answer,
                'score': _row.score,
                'value': _row.value,
            })

        return _answers

    @staticmethod
    def save_answers(user_id: int, restaurant_id: int, page_id: int, answers: list):
        _rows = []
        total_score = 0
        for item in answers:
            _tmp = {
                'user_id': user_id,
                'restaurant_id': restaurant_id,
                'page_id': page_id,
                'create_time': int(time.time())
            }
            _tmp = dict(_tmp, **item)
            total_score += int(item['score'])
            _rows.append(_tmp)

        print('total_score: ', total_score)

        try:
            query = (Answer
                     .replace_many(_rows)
                     .namedtuples())
            data = query.execute()
            if data:
                _record_query = (PageRecord.replace({
                    PageRecord.user_id: user_id,
                    PageRecord.restaurant_id: restaurant_id,
                    PageRecord.page_id: page_id,
                    PageRecord.total_score: total_score,
                }).namedtuples())
                _record = _record_query.execute()

            return bool(data) and bool(_record)
        except (TypeError, Exception):
            return False

    @staticmethod
    def save_bill(user_id: int, restaurant_id: int, page_id: int, bill_amount: int, tip: int, waiter):
        try:
            _query = (PageRecord.update({
                PageRecord.bill_amount: bill_amount,
                PageRecord.waiter: waiter,
                PageRecord.tip: tip,
            }).where((PageRecord.user_id == user_id) &
                     (PageRecord.restaurant_id == restaurant_id) &
                     (PageRecord.page_id == page_id))
                      .namedtuples())
            _record = _query.execute()

            return bool(_record)
        except (TypeError, Exception):
            return False


if __name__ == "__main__":

    print(DataUtil.get_all_questions(1))
    # print(DataUtil.get_one_question(12).question)

    # print(DataUtil.save_answers(1, 1, 1, [
    #     # {'question_id': '1', 'answer': 'Y'},
    #     {'question_id': '2', 'answer': 'N'},
    #     {'question_id': '3', 'answer': '100'},
    # ]))

    # print(DataUtil.get_answers(1, 1))

    # Option.insert_many([
    #     {'question_id': 1, 'option': 'Yes', 'value': 1, 'score': 10, 'order': 1},
    #     {'question_id': 1, 'option': 'No', 'value': 0, 'score': 5, 'order': 2},
    #     {'question_id': 2, 'option': 'Yes', 'value': 1, 'score': 10, 'order': 1},
    #     {'question_id': 2, 'option': 'No', 'value': 0, 'score': 5, 'order': 2},
    #     {'question_id': 3, 'option': 'Yes', 'value': 1, 'score': 10, 'order': 1},
    #     {'question_id': 3, 'option': 'No', 'value': 0, 'score': 5, 'order': 2},
    #     {'question_id': 4, 'option': 'Yes', 'value': 1, 'score': 10, 'order': 1},
    #     {'question_id': 4, 'option': 'No', 'value': 0, 'score': 5, 'order': 2},
    #     {'question_id': 5, 'option': 'Yes', 'value': 1, 'score': 10, 'order': 1},
    #     {'question_id': 5, 'option': 'No', 'value': 0, 'score': 5, 'order': 2},
    #     {'question_id': 6, 'option': 'Yes', 'value': 1, 'score': 10, 'order': 1},
    #     {'question_id': 6, 'option': 'No', 'value': 0, 'score': 5, 'order': 2},
    #     {'question_id': 7, 'option': 'Yes', 'value': 1, 'score': 10, 'order': 1},
    #     {'question_id': 7, 'option': 'No', 'value': 0, 'score': 5, 'order': 2},
    #
    #     {'question_id': 8, 'option': '1', 'value': 1, 'score': 1, 'order': 1},
    #     {'question_id': 8, 'option': '2', 'value': 2, 'score': 2, 'order': 2},
    #     {'question_id': 8, 'option': '3', 'value': 3, 'score': 3, 'order': 3},
    #     {'question_id': 8, 'option': '4', 'value': 4, 'score': 4, 'order': 4},
    #     {'question_id': 8, 'option': '5', 'value': 5, 'score': 5, 'order': 5},
    #     {'question_id': 8, 'option': '6', 'value': 6, 'score': 6, 'order': 6},
    #     {'question_id': 8, 'option': '7', 'value': 7, 'score': 7, 'order': 7},
    #     {'question_id': 8, 'option': '8', 'value': 8, 'score': 8, 'order': 8},
    #     {'question_id': 8, 'option': '9', 'value': 9, 'score': 9, 'order': 9},
    #     {'question_id': 8, 'option': '10', 'value': 10, 'score': 10, 'order': 10},
    #
    #     {'question_id': 9, 'option': '1', 'value': 1, 'score': 1, 'order': 1},
    #     {'question_id': 9, 'option': '2', 'value': 2, 'score': 2, 'order': 2},
    #     {'question_id': 9, 'option': '3', 'value': 3, 'score': 3, 'order': 3},
    #     {'question_id': 9, 'option': '4', 'value': 4, 'score': 4, 'order': 4},
    #     {'question_id': 9, 'option': '5', 'value': 5, 'score': 5, 'order': 5},
    #     {'question_id': 9, 'option': '6', 'value': 6, 'score': 6, 'order': 6},
    #     {'question_id': 9, 'option': '7', 'value': 7, 'score': 7, 'order': 7},
    #     {'question_id': 9, 'option': '8', 'value': 8, 'score': 8, 'order': 8},
    #     {'question_id': 9, 'option': '9', 'value': 9, 'score': 9, 'order': 9},
    #     {'question_id': 9, 'option': '10', 'value': 10, 'score': 10, 'order': 10},
    #
    #     {'question_id': 10, 'option': '1', 'value': 1, 'score': 1, 'order': 1},
    #     {'question_id': 10, 'option': '2', 'value': 2, 'score': 2, 'order': 2},
    #     {'question_id': 10, 'option': '3', 'value': 3, 'score': 3, 'order': 3},
    #     {'question_id': 10, 'option': '4', 'value': 4, 'score': 4, 'order': 4},
    #     {'question_id': 10, 'option': '5', 'value': 5, 'score': 5, 'order': 5},
    #     {'question_id': 10, 'option': '6', 'value': 6, 'score': 6, 'order': 6},
    #     {'question_id': 10, 'option': '7', 'value': 7, 'score': 7, 'order': 7},
    #     {'question_id': 10, 'option': '8', 'value': 8, 'score': 8, 'order': 8},
    #     {'question_id': 10, 'option': '9', 'value': 9, 'score': 9, 'order': 9},
    #     {'question_id': 10, 'option': '10', 'value': 10, 'score': 10, 'order': 10},
    # ]).namedtuples().execute()

    pass

