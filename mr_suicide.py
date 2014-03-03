import rg


class Robot:

    def act(self, game):
        close_enemy = self.enemy_close(game)
        if self.suicide_reason():
            return ['suicide']

        if close_enemy != 'none':
            return ['attack', close_enemy]

        if self.robot_on_position(game, self.add_to_defense()) != 'ally' and self.location != rg.CENTER_POINT:
            return ['move', rg.toward(self.location, rg.CENTER_POINT)]
        return ['guard']

    def look_arounds(self):
        for loc in rg.locs_around(self.location):
            (rg.loc_types(loc))

    def enemy_close(self, game):
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                if rg.dist(loc, self.location) <= 1:
                        return loc
        return 'none'

    def add_to_defense(self):
        rg.toward(self.location, rg.CENTER_POINT)


    def robot_on_position(self, game, loc):
        for x, robot in game.robots.iteritems():
            if robot.location == loc:
                if robot.player_id == self.player_id:
                    return 'ally'
                if robot.player_id != self.player_id:
                    return 'enemy'
        return 'empty'

    def suicide_reason(self):
        if self.hp <= 10:
            return True
        else :
            return False