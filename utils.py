class Utils():

	def is_element_present(self, how, what):
		try: self.driver.find_element(by=how, value=what)
		except NoSuchElementException as e: return False
		return True

	def click_element(self, webelement):
		try: webelement.click()
		except NoSuchElementException as e: return False
		return True

	def scroll_to_element(self, webelement):
		try: self.driver.execute_script("arguments[0].scrollIntoView();", webelement)
		except NoSuchElementException as e: return False
		return True

	def search_tag(self, list, tag):
		for i in range(len(list)):
			if list[i].text == tag:
				return True
			return False