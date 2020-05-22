# -*- coding:utf-8 -*-
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import time


def randomize(data, length=0):
    """Funcion  que incluye a un string pasado por parametro ``data``, un numero aleatorio. Opcionalmente
       se puede informar de la longitud del valor numerico ``length``.
            """
    longitud = 0 if length == 0 else 12 - length
    return data + "-" + str(time.time()).replace(".", "")[longitud:]


def today(US=False):
    """
    Funcion que devuelve el día actual en formato "DD-MM-AAAA"
    :return: Str de la fecha actual
    """
    if US:
        return datetime.today().strftime('%m-%d-%Y')
    else:
        return datetime.today().strftime('%d-%m-%Y')


def today_plus_days(days_to_add, US=False):
    """
    Funcion que devuelve la fecha actual mas los dias especificados en el parametro ``days_to_add´´.
    Devuelve el dia en formato "DD-MM-AAAA"
    :param days_to_add: Dias que se sumanar al dia actual
    :return: Str de la fecha del dia actual mas el numero de dias sumados
    """
    if US:
        return (datetime.now() + timedelta(days=int(days_to_add))).strftime('%m-%d-%Y')
    else:
        return (datetime.now() + timedelta(days=int(days_to_add))).strftime('%d-%m-%Y')


def first_month_day():
    """
    Funcion que devuelve la fecha del primer dia del mes actual. Devuelve el dia
    en formato "DD-MM-AAAA"
    :return: Str de la fecha del primer dia del mes actual
    """
    return datetime.now().replace(day=1).strftime('%d-%m-%Y')


def last_month_day():
    """
    Funcion que devuelve la fecha del ultimo dia del mes actual. Devuelve el dia en
    formato "DD-MM-AAAA"
    :return: Str de la fecha del ultimo dia del mes actual
    """
    return (datetime.now().replace(day=1) + relativedelta(months=1) + timedelta(days=-1)).strftime(
        '%d-%m-%Y')


def last_month_first_day():
    """
    Funcion que devuelve la fecha del ultimo dia del mes actual. Devuelve el dia en
    formato "DD-MM-AAAA"
    :return: Str de la fecha del ultimo dia del mes actual
    """
    return (datetime.now().replace(day=1) + relativedelta(months=-1) + timedelta(days=-1)).strftime(
        '%d-%m-%Y')


def today_substract_hours(hours_to_subtract=0, US=False):
    """
    Funcion que devuelve el día actual restandole las horas pasadas"
    :return: Str de la fecha actual
    """
    if US:
        return (datetime.now() - timedelta(hours=int(hours_to_subtract))).strftime('%m-%d-%Y %H:%M')
    else:
        return (datetime.now() - timedelta(hours=int(hours_to_subtract))).strftime('%d-%m-%Y %H:%M')


def today_plus_hours(hours_to_plus=0, US=False):
    """
    Funcion que devuelve el día actual sumandole las horas pasadas"
    :return: Str de la fecha actual
    """
    if US:
        return (datetime.now() + timedelta(hours=int(hours_to_plus))).strftime('%m-%d-%Y %H:%M')
    else:
        return (datetime.now() + timedelta(hours=int(hours_to_plus))).strftime('%d-%m-%Y %H:%M')


def today_substract_minutes(minutes_to_subtract=0, US=False):
    """
    Funcion que devuelve el día actual restandole los minutos pasados"
    :return: Str de la fecha actual
    """
    if US:
        return (datetime.now() - timedelta(minutes=int(minutes_to_subtract))).strftime(
            '%m-%d-%Y %H:%M')
    else:
        return (datetime.now() - timedelta(minutes=int(minutes_to_subtract))).strftime(
            '%d-%m-%Y %H:%M')


def today_plus_minutes(minutes_to_plus=0, US=False):
    """
    Funcion que devuelve el día actual sumandole los minutos pasados"
    :return: Str de la fecha actual
    """
    if US:
        return (datetime.now() + timedelta(minutes=int(minutes_to_plus))).strftime('%m-%d-%Y %H:%M')
    else:
        return (datetime.now() + timedelta(minutes=int(minutes_to_plus))).strftime('%d-%m-%Y %H:%M')


def date_substract_hours(date, hours_to_subtract=0, US=False):
    """
    Funcion que devuelve el día pasado por parametro restandole las horas pasadas"
    :return: Str de la fecha pasado por parametro
    """
    if US:
        dt_date = date if not isinstance(date, str) else datetime.strptime(date, '%m-%d-%Y %H:%M')
        return (dt_date - timedelta(hours=int(hours_to_subtract))).strftime('%m-%d-%Y %H:%M')
    else:
        dt_date = date if not isinstance(date, str) else datetime.strptime(date, '%d-%m-%Y %H:%M')
        return (dt_date - timedelta(hours=int(hours_to_subtract))).strftime('%d-%m-%Y %H:%M')


def date_plus_hours(date, hours_to_plus=0, US=False):
    """
    Funcion que devuelve el día pasado por parametro sumandole las horas pasadas"
    :return: Str de la fecha pasado por parametro
    """
    if US:
        dt_date = date if not isinstance(date, str) else datetime.strptime(date, '%m-%d-%Y %H:%M')
        return (dt_date + timedelta(hours=int(hours_to_plus))).strftime('%m-%d-%Y %H:%M')
    else:
        dt_date = date if not isinstance(date, str) else datetime.strptime(date, '%d-%m-%Y %H:%M')
        return (dt_date + timedelta(hours=int(hours_to_plus))).strftime('%d-%m-%Y %H:%M')


def date_substract_minutes(date, minutes_to_subtract=0, US=False):
    """
    Funcion que devuelve el día pasado por parametro restandole los minutos pasados"
    :return: Str de la fecha pasado por parametro
    """
    if US:
        dt_date = date if not isinstance(date, str) else datetime.strptime(date, '%m-%d-%Y %H:%M')
        return (dt_date - timedelta(minutes=int(minutes_to_subtract))).strftime(
            '%m-%d-%Y %H:%M')
    else:
        dt_date = date if not isinstance(date, str) else datetime.strptime(date, '%d-%m-%Y %H:%M')
        return (dt_date - timedelta(minutes=int(minutes_to_subtract))).strftime(
            '%d-%m-%Y %H:%M')


def date_plus_minutes(date, minutes_to_plus=0, US=False):
    """
    Funcion que devuelve el día pasado por parametro sumandole los minutos pasados"
    :return: Str de la fecha pasado por parametro
    """
    if US:
        dt_date = date if not isinstance(date, str) else datetime.strptime(date, '%m-%d-%Y %H:%M')
        return (dt_date + timedelta(minutes=int(minutes_to_plus))).strftime('%m-%d-%Y %H:%M')
    else:
        dt_date = date if not isinstance(date, str) else datetime.strptime(date, '%d-%m-%Y %H:%M')
        return (dt_date + timedelta(minutes=int(minutes_to_plus))).strftime('%d-%m-%Y %H:%M')