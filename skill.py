class Skill():
	time, cooltime
	useConditionSubject, useCondition, useConditionValue
	targetConditionSubject, targetCondition, targetConditionDetail
	additionalHitResultCondition, additionalHitResultConditionValue
	owner
	targets

	hitResults

	def OnStart(owner, targets):
		this.owner = owner
		this.targets = targets
		this.cooltime = originCooltime

		GenerateHitResults()

		pass

	def OnEnd():
		pass

	def OnUpdate(dt):
		pass

	def OnCanceled():
		pass

	def OnFire():
		pass

	def GenerateHitResults():
		generate hit results by skill data
