class bird(object):
    have_feather = True
    way_of_reproduction = 'egg'
    def move(self,dx,dy):
        position = [0,0]
        position[0]= position[0]+dx
        position[1]= position[1]+dy
        return position
    

    
summer = bird()
print summer.way_of_reproduction
print 'after move:',summer.move(5,8)


class chicken(bird):
      way_of_move = 'walk'
      possible_in_KFC = True

class oriole(bird):
    way_of_move = 'fly'
    possible_in_KFC = False

summer = chicken()
print summer.have_feather
print summer.move(5,8)
print summer.possible_in_KFC


class happybird(bird):
    def _init_(self,more_words):
        print 'we are happy birds,',more_words

summer = happybird()
summer._init_('happy,happy!')


