'use client'

import { MoveRight } from 'lucide-react'
import Link from 'next/link'
import React from 'react'

import { css } from '../../../styled-system/css'
import { hstack, vstack } from '../../../styled-system/patterns'
import { secondaryButton } from '../styles/reciepts/button'

interface IProps {
	className?: string
	name: string
	description: string
	price: number
	conditionals: string[]
}

const TarifCard = ({
	className,
	name,
	description,
	price,
	conditionals
}: IProps) => {
	const [isHover, setIsHover] = React.useState<boolean>(false)

	return (
		<Link
			onMouseLeave={() => setIsHover(false)}
			onMouseOver={() => setIsHover(true)}
			href={'#'}
			className={
				className +
				' ' +
				vstack({
					alignItems: 'start',
					textAlign: 'start',
					background: 'grayLight',
					borderRadius: '10px',
					padding: '25px 100px 45px 45px',
					fontSize: 'big',
					transitionDuration: '0.2s',

					_hover: {
						scale: '1.03',
						transitionDuration: '0.2s'
					}
				})
			}
		>
			<div className={css({ marginBottom: '10px' })}>
				<h4>{name}</h4>
				<p className={css({ fontSize: 'small', color: 'gray' })}>
					{description}
				</p>
			</div>
			<div className={secondaryButton()}>Попробовать</div>
			<p className={css({ color: 'gray' })}>
				<span className={css({ color: 'bkg' })}>{price}р / </span>в месяц
			</p>
			<ul>
				{conditionals.map((e, i) => (
					<li key={e + i} className={hstack()}>
						<div
							className={css({
								width: '15px',
								height: '15px',
								borderRadius: '50%',
								background: 'bkg'
							})}
						/>
						{e}
					</li>
				))}
			</ul>
			<div
				className={hstack({
					lineHeight: '1',
					color: isHover ? 'secondary' : 'gray',
					textTransform: 'uppercase',
					fontSize: 'common'
				})}
			>
				Подробнее
				<MoveRight size={40} />
			</div>
		</Link>
	)
}

export default TarifCard
