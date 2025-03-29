'use client'

import React from 'react'

import Navigation from '@/features/navigation/ui/Navigation'

import Logo from '@/shared/components/Logo'

import { css } from '../../../../styled-system/css'
import { hstack, vstack } from '../../../../styled-system/patterns'

import { useScreenSize } from '@/hooks/screenSize'

const Footer = () => {
	const screen = useScreenSize()

	return (
		<footer
			className={
				screen.width > 800
					? hstack({
							alignItems: 'start',
							color: 'primary',
							fontSize: screen.width > 1200 ? 'medium' : 'small',
							justifyContent: 'space-between',
							padding: '0 0 100px'
						})
					: vstack({
							color: 'primary',
							fontSize: 'small',
							padding: '0 0 50px',
							gap: '20px',
							alignItems: 'start'
						})
			}
		>
			<div className={css({ maxWidth: '360px' })}>
				<Logo />
				<p>
					Мы помогаем бизнесам эффективно исследовать рынок и разрабатывать
					обоснованные стратегии.
				</p>
			</div>
			<div className=''>
				<Navigation
					className={vstack({
						gap: '10px',
						fontSize: screen.width > 1200 ? 'medium' : 'small'
					})}
				/>
			</div>
			<div
				className={css({ fontSize: screen.width > 1200 ? 'big' : 'medium' })}
			>
				Главный офис
				<ul
					className={css({
						fontSize: screen.width > 1200 ? 'medium' : 'small'
					})}
				>
					<li>Телефон: 8 (9**)-**-**-***</li>
					<li>E-mail: Konkur@mail.ru</li>
					<li>Адрес: г. Краснодар, Серевная 405</li>
				</ul>
			</div>
		</footer>
	)
}

export default Footer
