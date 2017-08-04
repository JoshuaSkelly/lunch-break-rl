import instances
import palette

from entities import entity
from entities import player

regular_viewers = [
    'daemianend',
    'cuddigan',
    'fourbitfriday',
    'falseparklocation',
    'pythooonuser',
    'gui2203',
    'nimphious',
    'loggercito',
    'firedrgn',
    'kingdred405',
    'slayerdarth',
    'smyyth',
    'paspartout',
    'nixrod',
    'glasscaskettv',
    '109thanos'
]


class TwitchChatManager(entity.Entity):
    def __init__(self):
        super().__init__(' ')

    def handle_events(self, event):
        current_scene = instances.scene_root

        if event.type == 'TWITCHCHATMESSAGE':
            if event.message:
                if event.message.upper() == '!JOIN':
                    player_names = [e.name for e in current_scene.entities if hasattr(e, 'name')]

                    if not event.nickname in player_names:
                        # Set player color
                        if event.tags['subscriber'] != '0' and event.nickname != 'joshuaskelly':
                            player_color = palette.BRIGHT_BLUE

                        elif event.nickname.lower() in regular_viewers:
                            player_color = palette.BRIGHT_RED

                        else:
                            player_color = palette.get_nearest((255, 163, 0))

                        # Add player
                        p = player.Player(event.nickname[0], current_scene.get_location_near_stairs(), fg=player_color)
                        p.name = event.nickname
                        current_scene.entities.append(p)
                        instances.console.print('{} has joined!'.format(event.nickname))

                elif event.message.upper() == '!LEAVE':
                    for e in current_scene.entities:
                        if not isinstance(e, player.Player):
                            continue

                        if e.name == event.nickname:
                            e.die()
                            instances.console.print('{} has left.'.format(event.nickname))
