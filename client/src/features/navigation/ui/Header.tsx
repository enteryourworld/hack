import Link from 'next/link'
import React from 'react'

import Logo from '@/shared/components/Logo'

import { hstack } from '../../../../styled-system/patterns'

import Navigation from './Navigation'

const Header = () => {
	return (
		<header
			className={hstack({
				padding: '15px 0',
				justifyContent: 'space-between',
				width: '100%'
			})}
		>
			<Link href={'/'}>
				<Logo />
			</Link>
			<Navigation />
		</header>
	)
}

export default Header
