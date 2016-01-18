class Character():
	ability, dirtyAbility
	currState
	equipWeapon, equipAccessory

	def OnDead():
		pass

	def OnStateChanged():
		pass

	def OnSkillUsed():
		pass

	def OnUpdate():
		currState.OnUpdate(this)

		for buff in buffList:
			buff.OnUpdate(this)

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