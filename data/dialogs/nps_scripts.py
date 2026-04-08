NPC_FIRST_DIALOG_SCRIPT = "npc_dialog_1"
NPC_FIRST_DIALOG_END_SCRIPT = "npc_dialog_2"
NPC_CREATED_KEY_SCRIPT = "npc_dialog_3"
NPC_IS_CRAZY_SCRIPT = "npc_dialog_4"

import models.dialog_scripts as replics
from models.enitites.npc import NPC_NAME
from models.enitites.player import PLAYER_NAME

# ПЕРВЫЙ СЦЕНАРИЙ

replics.create_script(NPC_FIRST_DIALOG_SCRIPT)
replics.append_replic(NPC_NAME, "Ну привет... Я тут застрял немного. Как и ты, впочем...")
replics.append_replic(NPC_NAME, "Дверь спереди заперта, и чтобы открыть ее, понадобится ключь.")
replics.append_replic(PLAYER_NAME, "И где же достать этот ключь?")
replics.append_replic(NPC_NAME, "А не знаю. Но я помню, как он выглядел.")
replics.append_replic(NPC_NAME, "Принеси мне 1 глину и 2 серебра - я сделаю копию ключа и мы сможем выбраться")

# ВТОРОЙ СЦЕНАРИЙ

replics.create_script(NPC_FIRST_DIALOG_END_SCRIPT)
replics.append_replic(NPC_NAME, "Принеси мне 1 глину и 2 серебра")

# ТРЕТИЙ СЦЕНАРИЙ

replics.create_script(NPC_CREATED_KEY_SCRIPT)
replics.append_replic(NPC_NAME, "Я сделал! Я сделал! Я Сделал! Я Сделал! Я Сделал! Я Сделал! Я Сделал! Я Сделал! Я Сделал! Я Сделал! Я Сделал! Я Сделал! Я Сделал! Я Сделал! Я Сделал! Я Сделал! Я Сделал! Я Сделал! Я Сделал! Я Сделал! Я Сделал!")
replics.append_replic("", "Вы взяли ключь")

# ЧЕТВЕРТЫЙ СЦЕНАРИЙ

replics.create_script(NPC_IS_CRAZY_SCRIPT)
replics.append_replic(PLAYER_NAME, "Не стоит его тревожить...")
