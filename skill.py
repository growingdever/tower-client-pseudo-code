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
		this.time = 0

		GenerateHitResults()

	def OnEnd():
		pass

	def OnUpdate(dt):
		for index, pair in hitResults:
			hitResults[index].time -= dt
			if hitResults[index] < 0:
				OnFire(pair.hitResult)
				hitResults.remove(pair)

	def OnCanceled():
		pass

	def OnFire(hitResult):
		for target in targets:
			target.OnRecvHitResult(hitResult)

	def GenerateHitResults():
		generate hit results by skill data
