start_command_response =  "Привет, меня зовут Indigo!" \
                          "\n" \
                          "\n" \
                          "Я буду оповещать тебя о новых вебворках и оценках :)" \
                          "\n" \
                          "Все данные, которые ты доверишь мне будут в безопасности, поэтому можешь ни чуть не переживать." \
                          "\n" \
                          "\n" \
                          "Пропиши /help, чтобы увидеть список доступных команд." \
                          "\n" \
                          "\n" \
                          "Удачи и высокого GPA!"

empty_login_response = "Логин не должен быть пустым :)"

updated_login_response = "Прекрасно, я обновил твой логин!"

empty_password_response = "Пароль не должен быть пустым :)"

updated_password_response = "Замечательно, я обновил твой пароль!"

new_webwork_reponse = "New webwork!\n"

unknown_command_response = "Прости, но я не знаю эту команду.\nВведи /help, чтобы увидеть список доступных команд."

help_command_response = "Доступные команды:" \
                        "\n" \
                        "\n" \
                        "1. /set_username <your_username> - твой username это строка вида name.surname" \
                        "\n" \
                        "2. /set_main_password <your_password> - main_password это твой пароль от moodle и registrar" \
                        "\n" \
                        "3. /get_schedule - если ты сообщил мне правильные данные, этой командой я сохраню твое расписание, и ты сможешь обращаться к нему в любой момент" \
                        "\n" \
                        "4. /show_schedule - эта команда позволит тебе получать свое расписание в удобном формате" \
                        "\n" \
                        "5. /set_webwork_password <your_password> - обычно пароль от webwork'ов это твой Student ID" \
                        "\n" \
                        "6. /notify_webwork - если ты сообщил мне правильные данные, эта команда начнет оповещать тебя о новых webwork'ах в твоем аккаунте" \
                        "\n" \
                        "7. /help - показывает все доступные команды"

no_login_or_password_response = 'Пожалуйста укажи свой логин и пароль. \n \nВведи /help, если понадобится помощь.'

checking_data_response = 'Один момент. Я проверю твои данные.'

wrong_webwork_data_response = 'Похоже ты ввел неправильные данные, или ты не зарегистрирован ни на один из курсов :('

wrong_registrar_data_response = 'Похоже ты ввел неправильные данные, попробуй обновить свой логин и пароль.'

successful_webwork_login_response = 'Отлично! Теперь я буду уведомлять тебя о новых вебворках.\nНа данный момент у тебя есть следующие вебворки:'

successful_registrar_login_response = 'Круто! Я сохранил твое расписание, и теперь ты сможешь обращаться к нему в любой момент ^_^'

no_schedule_response = 'У меня нет твоего расписания :(\n\nНе забудь указать свои данные, а затем вызвать /get_schedule, чтобы я сохранил твое расписание.'