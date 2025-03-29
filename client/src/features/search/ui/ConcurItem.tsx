'use client'

import { MoveRight } from 'lucide-react'
import Image, { StaticImageData } from 'next/image'
import React from 'react'

import { css } from '../../../../styled-system/css'
import { circle, hstack } from '../../../../styled-system/patterns'

import { useScreenSize } from '@/hooks/screenSize'

interface IProps {
	className?: string
	bg: StaticImageData
}

const ConcurItem = ({ bg }: IProps) => {
	const screen = useScreenSize()

	return (
		<div
			className={css({
				background: 'gray',
				color: 'primary',
				padding: '20px 0 20px 30px',
				borderRadius: '35px',
				overflow: 'hidden',
				display: 'flex',
				flexDirection: 'column',
				gap: '15px',
				transitionDuration: '0.2s',
				position: 'relative',
				_hover: {
					scale: '1.03',
					transitionDuration: '0.2s'
				}
			})}
		>
			<div
				className={css({
					display: 'flex',
					alignItems: 'start',
					justifyContent: 'space-between',
					zIndex: '5'
				})}
			>
				{/* Image */}
				<div
					className={circle({
						background: 'primary',
						width: screen.width > 850 ? '120px' : '80px',
						height: screen.width > 850 ? '120px' : '80px'
					})}
				></div>
				<div
					className={css({
						background: 'rgba(53, 71, 125, 0.78)',
						padding:
							screen.width > 850
								? '18px 190px 18px 18px'
								: '10px 50px 10px 10px',
						display: 'flex',
						flexDirection: 'column',
						gap: screen.width > 850 ? '40px' : '15px',
						borderRadius: '10px',
						textAlign: 'start'
					})}
				>
					<div>
						<h5
							className={css({
								fontSize: screen.width > 850 ? 'big' : 'medium'
							})}
						>
							Компания
						</h5>
						<p className={css({ fontSize: 'small' })}>описание</p>
					</div>
					<div className=''>
						<h2 className={css({ fontSize: 'medium' })}>Соц. Сети</h2>
						<div className={hstack({ gap: '0' })}>
							<div
								className={circle({
									width: '30px',
									height: '30px',
									background: 'primary'
								})}
							></div>
							<div
								className={circle({
									width: '30px',
									height: '30px',
									background: 'primary',
									marginLeft: '-10px'
								})}
							></div>
							<div
								className={circle({
									width: '30px',
									height: '30px',
									background: 'primary',
									marginLeft: '-10px'
								})}
							></div>
						</div>
					</div>
				</div>
			</div>
			<button
				type='button'
				className={hstack({
					fontSize: screen.width > 850 ? 'medium' : 'small',
					alignSelf: 'end',
					paddingRight: '30px',
					zIndex: '10'
				})}
			>
				ПОДРОБНЕЕ
				<MoveRight />
			</button>
			<Image
				src={bg}
				alt='bg'
				className={css({
					position: 'absolute',
					top: '0',
					left: '0',
					width: '100%',
					height: '100%',
					objectFit: 'cover',
					zIndex: '0'
				})}
			/>
		</div>
	)
}

export default ConcurItem
