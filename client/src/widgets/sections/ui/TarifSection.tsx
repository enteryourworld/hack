'use client'

import React from 'react'

import TarifCard from '@/shared/components/TarifCard'

import { css } from '../../../../styled-system/css'
import { hstack, vstack } from '../../../../styled-system/patterns'

import { useScreenSize } from '@/hooks/screenSize'

const TarifSection = () => {
	const tarifList = [
		{
			id: 1,
			name: 'Базовый',
			description: 'Для небольших команд',
			price: 900,
			conditionsList: ['Условие', 'Условие', 'Условие']
		},
		{
			id: 2,
			name: 'Базовый',
			description: 'Для небольших команд',
			price: 900,
			conditionsList: ['Условие', 'Условие', 'Условие']
		},
		{
			id: 3,
			name: 'Базовый',
			description: 'Для небольших команд',
			price: 900,
			conditionsList: ['Условие', 'Условие', 'Условие']
		}
	]

	const screen = useScreenSize()

	return (
		<section
			className={vstack({
				gap: '50px',
				fontSize: 'large',
				textAlign: 'center',
				background: 'primary',
				padding: '150px 50px 70px',
				marginBottom: 'between_section'
			})}
		>
			<div className=''>
				<h3>Тарифный план</h3>
				<p className={css({ color: 'gray', fontSize: 'common' })}>
					Выбери свои выгодные условия
				</p>
				<div
					className={
						screen.width > 1150
							? hstack({ gap: '30px', marginTop: '60px' })
							: vstack({ gap: '30px', marginTop: '40px' })
					}
				>
					{tarifList.map(e => (
						<TarifCard
							name={e.name}
							key={e.id}
							description={e.description}
							price={e.price}
							conditionals={e.conditionsList}
						/>
					))}
				</div>
			</div>
		</section>
	)
}

export default TarifSection
