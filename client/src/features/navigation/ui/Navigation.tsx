import Link from 'next/link'
import React from 'react'

import { hstack } from '../../../../styled-system/patterns'

interface INavListItem {
	text: string
	href: string
}

const Navigation = () => {
	const list: INavListItem[] = [
		{
			text: 'Главная',
			href: '/'
		},
		{
			text: 'Ресурсы',
			href: '/resoures'
		},
		{
			text: 'Тарифы',
			href: '/tarifs'
		},
		{
			text: 'История поиска',
			href: '/search-history'
		},
		{
			text: 'Сравнение',
			href: '/sravni'
		}
	]

	return (
		<nav className={hstack({ fontSize: 'common' })}>
			<ul className={hstack({ gap: '30px', color: 'primary' })}>
				{list.map((e, i) => (
					<li key={e.text + i}>
						<Link href={e.href}>{e.text}</Link>
					</li>
				))}
			</ul>
		</nav>
	)
}

export default Navigation
