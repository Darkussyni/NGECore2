import sys

def setup(core, actor, buff):
	if actor.getSkillMod('expertise_buff_duration_line_me_enhance'):
		buff.setDuration(buff.getDuration()+(actor.getSkillModBase('expertise_buff_duration_line_me_enhance')))
	return

def add(core, actor, buff):
	core.skillModService.addSkillMod(actor, 'agility_modified', 15)
	return
	
def remove(core, actor, buff):
	core.skillModService.deductSkillMod(actor, 'agility_modified', 15)
	return
	