'use client'

import { MoveRight } from 'lucide-react'
import Image from 'next/image'
import Link from 'next/link'
import React from 'react'

import { css } from '../../../../styled-system/css'
import { hstack, vstack } from '../../../../styled-system/patterns'

import BG from '@/../public/images/main-section-bkg.jpg'
import { useScreenSize } from '@/hooks/screenSize'

const MainSection = () => {
	const screenSize = useScreenSize()

	return (
		<section
			className={css({
				background: 'primary',
				padding: screenSize.width > 870 ? '80px 60px 50px' : '40px 30px 25px',
				marginBottom: 'between_section'
			})}
		>
			<div
				className={vstack({
					position: 'relative',
					shadow: 'around',
					padding: '30px'
				})}
			>
				<div
					className={
						screenSize.width > 870
							? hstack({ width: '100%', justifyContent: 'space-between' })
							: vstack({ alignItems: 'center', width: '100%' })
					}
				>
					<h2
						className={css({
							fontSize:
								screenSize.width > 1200
									? 'large'
									: screenSize.width > 870
										? '36px'
										: screenSize.width > 650
											? 'medium'
											: 'common',
							textAlign: 'center',
							fontWeight: 'medium'
						})}
					>
						Закажи полный
						<br />
						разбор твоего
						<br />
						бизнеса!
					</h2>
					<Image
						src={BG}
						alt={'backround'}
						className={css({ width: screenSize.width > 870 ? '55%' : '70%' })}
					/>
				</div>
				<Link
					href={'/tarifs'}
					className={hstack({
						alignSelf: 'end',
						fontSize: 'common',
						paddingBottom: '5px',
						fontWeight: '500',

						_hover: {
							paddingBottom: '3px',
							borderBottom: '2px solid #000'
						}
					})}
				>
					Узнать больше
					<MoveRight />
				</Link>
			</div>
		</section>
	)
}

export default MainSection
