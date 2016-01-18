class Character():
	ability, dirtyAbility
	equipWeapon, equipAccessory
	currState
	skillList, currUsingSkill

	def OnDead():
		pass

	def OnStateChanged():
		pass

	def OnSkillStart(skill, targets):
		skill.OnStart(this, targets)
		currUsingSkill = skill
		pass

	def OnSkillEnd():
		pass

	def OnUpdate():
		currState.OnUpdate(this)

		for buff in buffList:
			buff.OnUpdate(this)

		currUsingSkill.OnUpdate()

		pass

	def OnStatusChanged():
		dirtyAbility = ability
		
		for buff in buffList:
			if buff.type == 'UPGRADE':
				buff.apply(dirtyAbility)

		equipWeapon.apply(dirtyAbility)
		equipAccessory.apply(dirtyAbility)

	def OnSendHitResult(hitResult):
		for buff in buffList:
			if buff.type == 'ADDITIONAL_HIT_RESULT':
				buff.OnSendHitResult(hitResult)
		pass

	def OnRecvHitResult(hitResult):
		dirtyAbility.apply(hitResult)

		for buff in buffList:
			if buff.type == 'REACT':
				buff.OnRecvHitResult(hitResult)
		pass

	def OnStepChanged():
		pass

	def OnStageChanged():
		pass