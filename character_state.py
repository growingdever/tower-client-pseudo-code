class CharacterState():
	owner

	def OnUpdate(character):
		pass
	pass


class CharacterStateIdle(CharacterState):
	def OnUpdate(character):
		base.OnUpdate(character)

		for skill in character.skillList:
			# 사용 조건 만족 체크
			if skill.cooltime > 0:
				continue
			if not battleManager.Usable(skill):
				continue

			# 대상 조건으로 대상 몬스터 찾음
			# 단일 대상 스킬이라도 대상은 리스트로 관리(일관성 때문)
			# target = skill.FindTargets()
			targets = battleManager.FindTargets(skill)
			if len(targets) == 0:
				continue

			skill.Start(this.owner, targets)
	pass