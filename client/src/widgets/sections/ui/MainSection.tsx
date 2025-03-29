import { MoveRight } from 'lucide-react'
import Image from 'next/image'
import Link from 'next/link'
import React from 'react'

import { css } from '../../../../styled-system/css'
import { hstack, vstack } from '../../../../styled-system/patterns'

import BG from '@/../public/images/main-section-bkg.jpg'

const MainSection = () => {
	return (
		<section
			className={css({
				background: 'primary',
				padding: '80px 60px 50px',
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
					className={hstack({ width: '100%', justifyContent: 'space-between' })}
				>
					<h2
						className={css({
							fontSize: 'large',
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
					<Image src={BG} alt={'backround'} width={740} />
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
