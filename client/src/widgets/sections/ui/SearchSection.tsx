'use client'

import React from 'react'

import ConcurItem from '@/features/search/ui/ConcurItem'
import Search from '@/features/search/ui/Search'

import { css } from '../../../../styled-system/css'
import { vstack } from '../../../../styled-system/patterns'

import BG1 from '@/../public/images/bg/close_up_building_model_maquette_design_construction_plan_table.jpg'
import BG2 from '@/../public/images/bg/contemporary-room-workplace-office-supplies-concept.jpg'
import BG3 from '@/../public/images/bg/girl_signs_documents_lady_sitting_table_manager_working_office.jpg'
import BG4 from '@/../public/images/bg/hands-writing-business-documents-desk-concept.jpg'
import BG5 from '@/../public/images/bg/millennial_asia_businessmen_businesswomen_meeting_brainstorming.jpg'
import BG6 from '@/../public/images/bg/paperwork.jpg'
import { useScreenSize } from '@/hooks/screenSize'

const SearchSection = () => {
	const list = [1, 2, 3, 4]
	const bgList = [BG1, BG2, BG3, BG4, BG5, BG6]

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
			<h2>
				Найди своего
				<br />
				конкурента
			</h2>
			<Search className={css({ width: '90%' })} />
			<div
				className={css({
					display: 'grid',
					padding: screen.width > 850 ? '40px' : 0,
					gap: '15px',
					gridTemplateColumns: screen.width > 1200 ? 'repeat(2, 1fr)' : '1fr',
					background: screen.width > 850 ? 'grayLight' : 'none',
					width: '100%'
				})}
			>
				{list.map((e, i) => (
					<ConcurItem key={i} bg={bgList[i % 6]} />
				))}
			</div>
		</section>
	)
}

export default SearchSection
