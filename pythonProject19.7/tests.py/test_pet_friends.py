import json
import os

from api import PetFriends
from settings import *

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_all_pets_whith_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0


def test_successful_add_new_pet_with_valid_data(name='Барбоскин', animal_type='двортерьер', age='4', pet_photo='dog.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), 'images', pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Супепес", "собака", "3", "images/dog.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("У меня нет животных")


def test_add_photo(pet_photo='dog2.jpeg'):
    """Проверяем возможность добавления фото для уже существующего питомца"""
    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), 'images', pet_photo)

    # Запрашиваем ключ api и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, добавляем фото
    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
        assert status == 200
        assert result['pet_photo'] != ''
    else:
        raise Exception(
            "У меня нет животных")  # если спиок питомцев пустой, то выкидываем исключение с
        # текстом об отсутствии своих питомце


def test_create_pet_simple_with_valid_data(name='Зюзя', animal_type='собака', age='3'):
    """Проверяем что можно добавить питомца с корректными данными, без фото"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.create_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_negative_add_new_pet_with_invalid_photo(name='Коржик', animal_type='кот', age='4', pet_photo='pfoto.txt'):
    """Негативный тест. Проверяем, что при добавлении фото в неверном формате, у нвс не
    получится создать нового питомца"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), 'images', pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Ожидаем, что новый питомец не будет создан, из-за неверного формата фото
    assert status == 400
    assert result['name'] == name


def test_negative_create_pet_simple_with_invalid_data(name='Зюзя', animal_type='собака', age='кошка'):
    """Негативный тест. Проверяем, что нельзя добавить питомца когда в поле age содержится слово"""


    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.create_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    assert result['name'] == name


def test_negative_get_api_key_for_invalid_user(email='invalid@m.ru', password=valid_password):
    """Негативный тестю Проверяем, что при неверно введенном "email" пользователь не сможет получить ключ"""
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result


def test_negative_add_photo(pet_photo='dog2.jpeg'):
    """Негативный тест. Проверяем что нельзя добавить фото для питомца другого пользователя"""
    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), 'images', pet_photo)

    # Запрашиваем ключ api и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key)

    # Если список не пустой, добавляем фото
    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
        assert status != 200
    else:
        raise Exception(
            "У меня нет животных")


def test_negative_delete_not_my_pet():
    """Негативный тест. Проверяем, что нельзя удалить питомца другого пользователя"""

    # Получаем ключ auth_key и запрашиваем список всех питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Получаем множество с id питомцев других пользователей
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    _, all_pets = pf.get_list_of_pets(auth_key)
    set_my_pets = {pet['id'] for pet in my_pets['pets']}
    set_all_pets = {pet['id'] for pet in all_pets['pets']}
    not_my_pets = set_all_pets - set_my_pets


    # Берём id питомца из списка и отправляем запрос на удаление
    pet_id = not_my_pets.pop()
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список чужих питомцев
    _, not_my_pets = pf.get_list_of_pets(auth_key)

    # Проверяем что статус ответа не равен 200 и в списке чужих питомцев остался id питомца
    assert status != 200
    assert pet_id in not_my_pets.values()


def test_negative_update_self_pet_info(name='Мурзик', animal_type='Котэ', age='два года'):
    """Негативный тест. Проверяем, что поле age не принимает текст"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа не 200
        assert status != 200
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("У меня нет животных")


def test_negativ_get_all_pets_whith_valid_key(filter=''):
    """Негативный тест. Проверяем, что нельзя пролучить список питомцев при неверном api_key"""
    status, result = pf.get_list_of_pets({'key': '123451'}, filter)
    assert status == 403


def test_negative_add_new_pet_with_invalid_key(name='', animal_type='', age='', pet_photo='dog.jpg'):
    """Негативный тест. Проверяем, что нельзя добавить питомца при неверном api_key"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), 'images', pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    # _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet({'key': '123451'}, name, animal_type, age, pet_photo)

    # Ожидаем, что новый питомец не будет создан, из-за неверного ключа
    assert status == 403