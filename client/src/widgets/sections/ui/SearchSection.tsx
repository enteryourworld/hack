import React from 'react'

import { vstack } from '../../../../styled-system/patterns'

const SearchSection = () => {
	return (
		<section className={vstack({ gap: '50px' })}>
			<h2>
				Найди своего
				<br />
				конкурента
			</h2>
		</section>
	)
}

export default SearchSection
