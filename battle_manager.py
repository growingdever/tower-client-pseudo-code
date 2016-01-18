class BattleManager():
	playerParty, enemyParty

	def Usable(skill):
		if skill.useConditionSubject == 'None':
			return True

		characters = [playerParty, enemyParty]
		filteredCharacters = []
		if skill.useConditionSubject == 'FriendsNotMe':
			for character in characters:
				if character.team != skill.owner.team:
					continue
				if character == skill.owner:
					continue
				filteredCharacters.append(character)

		if skill.useCondition == 'Die':
			for character in filteredCharacters:
				if character.IsDead():
					return True
		elif skill.useCondition == 'Exist':
			return len(filteredCharacters) > 0
		elif skill.useCondition == 'HP_LT':
			for character in filteredCharacters:
				if character.hp < useConditionValue:
					return True
			return False


	def FindTarget(skill):
		characters = [playerParty, enemyParty]
		filteredCharacters = []
		if skill.targetConditionSubject == 'FriendsNotMe':
			for character in characters:
				if character.team != skill.owner.team:
					continue
				if character == skill.owner:
					continue
				filteredCharacters.append(character)

		targets = []
		if skill.targetCondition == 'HP':
			if skill.targetConditionDetail == 'HIGHEST':
				SortByHPInDescendingOrder(targets)
				return targets[:0] # list slicing
			if skill.targetConditionDetail == 'LOWEST':
				SortByHPInDescendingOrder(targets)
				return targets[len(targets):] # list slicing
