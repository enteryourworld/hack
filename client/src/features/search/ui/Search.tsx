'use client'

import { ChevronUp } from 'lucide-react'
import React from 'react'

import { button } from '@/shared/styles/reciepts/button'

import { css } from '../../../../styled-system/css'
import { hstack } from '../../../../styled-system/patterns'

import Filters from './Filters'

interface IProps {
	className?: string
}

const Search = ({ className }: IProps) => {
	const [isFilterOpen, setIsFilterOpen] = React.useState<boolean>(false)

	return (
		<form action='' className={className + ' ' + css({ position: 'relative' })}>
			<div className={css({ marginBottom: '100px' })}>
				<input
					type='text'
					placeholder='Найти'
					className={css({
						fontSize: 'medium',
						border: '1px solid rgba(0, 0, 0, 0.5)',
						padding: '15px 25px',
						width: '100%'
					})}
				/>
				<div
					className={hstack({
						justifyContent: 'space-between',
						width: '100%',
						fontSize: 'small'
					})}
				>
					<p className={css({ color: 'gray' })}>Например: https://vk.ru/mts</p>
					<button
						type={'button'}
						onClick={() => setIsFilterOpen(!isFilterOpen)}
						className={hstack({
							fontWeight: '400',
							fontSize: 'common',
							gap: '2px',
							paddingBottom: '3px',
							cursor: 'pointer',
							_hover: {
								paddingBottom: '1px',
								borderBottom: '2px solid #000'
							}
						})}
					>
						Фильтр
						<ChevronUp
							size={20}
							className={css({
								rotate: isFilterOpen ? '180deg' : 'auto',
								transitionDuration: '0.2s'
							})}
						/>
					</button>
				</div>
				{isFilterOpen && <Filters />}
			</div>
			<button type='submit' className={button()}>
				Найти
			</button>
		</form>
	)
}

export default Search
