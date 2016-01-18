class Character():
	ability
	currState

	def OnDead():
		pass

	def OnStateChanged():
		pass

	def OnSkillUsed():
		pass

	def OnUpdate():
		dirtyAbility = ability
		for buf in bufList:
			buf.apply(dirtyAbility)

		currState.OnUpdate(this)

		pass

	def OnStepChanged():
		pass

	def OnStageChanged():
		pass