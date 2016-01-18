class Skill():
	time, delay, interval
	useConditionSubject, useCondition, useConditionValue
	targetConditionSubject, targetCondition, targetConditionDetail
	additionalHitResultCondition, additionalHitResultConditionValue
	owner
	targets

	def OnStart(owner, targets):
		this.owner = owner
		this.targets = targets
		delay = originCooltime
		pass

	def OnEnd():
		pass

	def OnUpdate():
		pass

	def OnCanceled():
		pass

	def OnFire():
		pass
