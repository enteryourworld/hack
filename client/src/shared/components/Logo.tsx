import Image from 'next/image'
import React from 'react'

import { css } from '../../../styled-system/css'
import { hstack } from '../../../styled-system/patterns'

import LOGO from '@/../public/images/logo.svg'

const Logo = () => {
	return (
		<div className={hstack()}>
			<Image src={LOGO} alt='logo picture' />
			<h3
				className={css({
					color: 'primary',
					fontSize: '3xl',
					letterSpacing: '-1.5%',
					fontWeight: '500'
				})}
			>
				Konkur
			</h3>
		</div>
	)
}

export default Logo
