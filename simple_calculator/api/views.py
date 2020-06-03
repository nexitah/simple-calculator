# -*- coding: utf-8 -*-
import json

from pyramid.response import Response
from pyramid.view import view_config

from simple_calculator.calculator.calculator import Calculator


class BasicCalculatorView:
    def __init__(self, request):
        self.request = request
        self.body = request.body

    @view_config(route_name='calculator', renderer='json', request_method='POST')
    def post(self):
        """
        Return the operation of the requested values
        :return:
        """
        if self.body == b'':
            return Response(
                status=400, json_body={
                    'result': 'Body is empy, please provide an operation!'
                })
            
        body = json.loads(self.body.decode("utf-8"))
        calculator = Calculator(operation=body.get('operation'))
        success, result = calculator.calculate()

        if not success:
            return Response(status=400, json_body={'result': result})

        return Response(status=200, json_body={'result': result})

    @view_config(route_name='calculator', renderer='json', request_method='GET')
    def get(self):
        """
        Return the operation of the requested values
        :return:
        """
        return Response(
            status=200,
            json_body={'result': 'To try this new shinny simple_calculator use the POST'})
