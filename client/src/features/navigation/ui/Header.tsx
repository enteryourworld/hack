'use client'

import { Menu, User } from 'lucide-react'
import Link from 'next/link'
import React from 'react'

import Logo from '@/shared/components/Logo'

import { css } from '../../../../styled-system/css'
import { hstack } from '../../../../styled-system/patterns'

import Navigation from './Navigation'
import { useScreenSize } from '@/hooks/screenSize'

const Header = () => {
	const screen = useScreenSize()

	return (
		<header
			className={hstack({
				padding: '30px 0',
				justifyContent: 'space-between',
				width: '100%'
			})}
		>
			<Link href={'/'}>
				<Logo />
			</Link>
			{screen.width > 960 ? (
				<>
					<Navigation className={hstack({ gap: '30px', color: 'primary' })} />
					<User className={css({ color: 'primary' })} />
				</>
			) : (
				<Menu color='#fff' />
			)}
		</header>
	)
}

export default Header
